"""Parcel data model for FarmChat.

This module defines the data model for agricultural parcels,
including validation and data processing methods.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Parcel(BaseModel):
    """Model representing an agricultural parcel."""
    
    id: str = Field(..., description="Unique identifier for the parcel")
    address: Optional[str] = Field(None, description="Physical address of the parcel")
    coordinates: Optional[tuple[float, float]] = Field(None, description="Latitude and longitude")
    created_at: datetime = Field(default_factory=datetime.now)
    
    def to_dict(self) -> dict:
        """Convert parcel data to dictionary format.
        
        Returns:
            dict: Parcel data as dictionary
        """
        return self.model_dump()
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Parcel':
        """Create a Parcel instance from dictionary data.
        
        Args:
            data: Dictionary containing parcel data
            
        Returns:
            Parcel: New Parcel instance
        """
        return cls(**data) 