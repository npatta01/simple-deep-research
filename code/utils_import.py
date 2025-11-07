# Utility helpers for the LangGraph notebook

import dotenv
import os

# Tracing imports are optional and only used when init_tracer is called
from opentelemetry import trace
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor


# Load local environment file used by the workshop
# Keep the same relative path as the notebook used
dotenv.load_dotenv("../env_workshop")

OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
PHOENIX_PROJECT_NAME = os.environ.get("PHOENIX_PROJECT_NAME")


# configure the Phoenix tracer
if os.environ.get("PHOENIX_COLLECTOR_ENDPOINT"):
    tracer_provider = register(
        project_name=PHOENIX_PROJECT_NAME, 
        auto_instrument=False 
    )
    
else:
    tracer_provider = trace.NoOpTracerProvider()

LangChainInstrumentor().instrument(tracer_provider=tracer_provider)
tracer = trace.get_tracer(__name__)

