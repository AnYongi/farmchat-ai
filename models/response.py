"""Response model for FarmChat.

This module defines the data model for formatting and structuring
API responses and chat messages.
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class ChatResponse(BaseModel):
    """Model for formatting chat responses."""
    
    message: str = Field(..., description="The response message")
    data_source: Literal["NIAST", "KMA"] = Field(..., description="Source of the data")
    timestamp: datetime = Field(default_factory=datetime.now)
    raw_data: Optional[dict] = Field(None, description="Raw API response data")
    
    def format_message(self) -> str:
        """Format the response message with metadata.
        
        Returns:
            str: Formatted response message
        """
        return f"""
        {self.message}
        
        Data Source: {self.data_source}
        Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        """
    
    def to_dict(self) -> dict:
        """Convert response to dictionary format.
        
        Returns:
            dict: Response data as dictionary
        """
        return self.model_dump() 