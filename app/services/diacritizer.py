from mishkal.tashkeel import TashkeelClass
import threading

class DiacritizerService:
    def __init__(self):
        self._local = threading.local()

    def _get_vocalizer(self):
        """Ensure each thread has its own TashkeelClass instance."""
        if not hasattr(self._local, "vocalizer"):
            self._local.vocalizer = TashkeelClass()
        return self._local.vocalizer

    def diacritize(self, text: str) -> str:
        vocalizer = self._get_vocalizer()
        return vocalizer.tashkeel(text)
