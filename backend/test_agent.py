from camel.models import BaseModelBackend, ModelFactory, ModelManager, OpenAIAudioModels, ModelProcessingError
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent

model = ModelFactory.create(
    model_platform=ModelPlatformType.LITELLM,
    model_type="hosted_vllm/qwen3",         # Using enum
    url="http://192.168.130.24:8000/v1",
    model_config_dict={"temperature": 0.0, "max_tokens": 1000},
)

agent_6 = ChatAgent("You are a helpful assistant.", model=model)
response = agent_6.step("Hello, how are you?")
print(response.msgs[0].content)
