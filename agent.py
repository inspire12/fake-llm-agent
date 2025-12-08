from tools import get_weather


class LlmAgent:
    def handle(self, user, message):
        if "날씨" in message:
            weather = get_weather("서울")
            return f"{user}님, 날씨는 '{weather}' 입니다."

        # 아주 단순한 LLM 흉내
        return f"{user}님, '{message}' 잘 받았습니다."
