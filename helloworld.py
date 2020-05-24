from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-cased')
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-cased')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True)).unsqueeze(0)  # Batch size 1
start_positions = torch.tensor([1])
end_positions = torch.tensor([3])
outputs = model(input_ids, start_positions=start_positions, end_positions=end_positions)
print()
print(outputs)
print()
loss, start_scores, end_scores = outputs[:3]

