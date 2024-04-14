from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData
import time


def process_agent_data(data: AgentData) -> ProcessedAgentData:
    state = "good"
    if 10 <= data.gps.longitude <= 19:
        state = "normally"
    elif data.gps.longitude >= 20:
        state = "bad"
    return ProcessedAgentData(road_state=state,
                              agent_data=data)
