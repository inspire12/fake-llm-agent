from tools import get_weather

class LlmAgent:
  def handle(self, user, message):
    if "날씨" in message:
      weather = get_weather("서울")
      return f"[LLM] {user}님, 서울 날씨는 {weather}입니다."

    return f"[LLM] {user}님, '{message}' 잘 받았습니다."
