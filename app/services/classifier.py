class ClassifyTicket:
  def classify(self, description: str):
    text = description.lower()
    category = self.__get__category(text)
    priority = self.__get__priority(text)
    
    return {
      "category": category,
      "priority": priority,
      "confidence": 0.85
    }
    
  def __get__category(self, text: str) -> str:
    if any(word in text for word in ["bug", "error", "crash", "broken", "server"]):
      return "technical"
    elif any(word in text for word in ["payment", "invoice", "refund", "billing"]):
      return "billing"
    elif any(word in text for word in ["login", "password", "account"]):
      return "account"
    else:
      return "other"
    
  def __get__priority(self, text: str) -> str:
    if any(word in text for word in ["urgent", "critical", "down", "asap"]):
      return "high"
    if any(word in text for word in ["minor", "typo", "suggestion"]):
      return "low"
    else:
      return "medium"
      
classifier = ClassifyTicket()