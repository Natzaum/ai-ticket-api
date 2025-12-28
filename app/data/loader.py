import pandas as pd
from pathlib import Path

class DatasetLoader:
  def __init__(self, filepath: str = "app/data/tickets_dataset.csv"):
    self.filepath = filepath
    self.df = None
    
  def load(self):
    if not Path(self.filepath).exists():
      raise FileNotFoundError(f"File not found: {self.filepath}")
    self.df = pd.read_csv(self.filepath)
    return self.df
  
  def get_all(self):
    if self.df is None:
      self.load()
    return self.df
  
  def get_by_category(self, category: str):
    if self.df is None:
      self.load()
    if self.df is None:
      raise ValueError("Failed to load dataset")
    return self.df[self.df['category'] == category]
  
  def get_by_priority(self, priority: str):
    if self.df is None:
      self.load()
    if self.df is None:
      raise ValueError("Failed to load dataset")
    return self.df[self.df['priority'] == priority]
  
  def get_stats(self):
    if self.df is None:
      self.load()
    if self.df is None:
      raise ValueError("Failed to load dataset")
        
    return {
      "total_tickets": len(self.df),
      "categories": self.df['category'].value_counts().to_dict(),
      "priorities": self.df['priority'].value_counts().to_dict()
    }