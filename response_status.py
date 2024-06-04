from enum import Enum

class ResponseStatus(Enum):
  PENDING = "pending"
  FULFILLED = "fulfilled"
  REJECTED = "rejected"
