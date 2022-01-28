from fastapi import Body, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, constr
from transformers import BertTokenizerFast, BertConfig, BertForSequenceClassification, default_data_collator
from accelerate import Accelerator
import torch
from torch.utils import data
from torch.utils.data import DataLoader
import warnings
warnings.filterwarnings('ignore')
warnings.warn('DelftStack')
warnings.warn('Do not show this message')

class QNLIRequest(BaseModel):
    question: constr(max_length=256)
    sentence: constr(max_length=256)

class Dataset(torch.utils.data.Dataset):
  def __init__(self, encodings):
    self.encodings = encodings

  def __getitem__(self, idx):
    return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

  def __len__(self):
    return len(self.encodings.input_ids)

def QNLI_model_predict(model, question, sentence):
    input_encodings = tokenizer([question], [sentence], padding='max_length', truncation=True, max_length=256)
    input_dataset = Dataset(input_encodings)

    data_collator = default_data_collator
    input_dataloader = DataLoader(input_dataset, collate_fn=data_collator, batch_size=1)  

    accelerator = Accelerator()
    model, input_dataloader = accelerator.prepare(model, input_dataloader)

    for batch in input_dataloader:
        outputs = model(**batch)
        predicted = outputs.logits.argmax(dim=-1)
    return predicted


app = FastAPI(
    title="QNLI",
    description="QNLI dataset training",
    version="1",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
config = BertConfig.from_pretrained("qnli_config.json") 
qnli_model = BertForSequenceClassification.from_pretrained("qnli_model.bin", config = config)

@app.get("/")
async def root():
    return RedirectResponse("docs")


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    return templates.TemplateResponse(f"{page_name}.html", {"request": request})


@app.post("/qnli")
async def qnli(
    qnli_request: QNLIRequest = Body(
        None,
        
    )
):

    results = QNLI_model_predict(qnli_model, qnli_request.question, qnli_request.sentence).item()

    if results:
        result = "not_entailment"
    else:
        result = "entailment"
    return result

