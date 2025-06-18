import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)
from datasets import Dataset
import os
import json

# === Config ===
MODEL_NAME = "distilbert-base-uncased"
DATA_PATH = "C:/Users/grace/Desktop/ai-mvp-suite/models/asad_nlp/intent_data.csv"
OUTPUT_DIR = "C:/Users/grace/Desktop/ai-mvp-suite/models/asad_nlp/asad_intent_model"

# === Load data ===
df = pd.read_csv(DATA_PATH)
df = df.dropna()

# === Encode labels ===
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["label"])
label_map = {label: int(idx) for idx, label in enumerate(label_encoder.classes_)}

# Save label map for inference
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "label_map.json"), "w") as f:
    json.dump(label_map, f)

# === Split data ===
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["text"], df["label"], test_size=0.2, stratify=df["label"], random_state=42
)

# === Load tokenizer ===
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# === Tokenize ===
train_dataset = Dataset.from_dict({"text": train_texts.tolist(), "label": train_labels.tolist()})
val_dataset = Dataset.from_dict({"text": val_texts.tolist(), "label": val_labels.tolist()})

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True)

train_dataset = train_dataset.map(tokenize, batched=True)
val_dataset = val_dataset.map(tokenize, batched=True)

# === Load model ===
num_labels = len(label_encoder.classes_)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=num_labels)

# === Training setup ===
args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=4,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss"
)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

# === Train ===
trainer.train()

# === Save model ===
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("✅ Training complete. Model saved to:", OUTPUT_DIR)
