# CryptoChatbot

Stack:
- Python
  - Tkinter 
  - Socket
  - BeautifulSoup
- Azure


Projekt zaliczeniowy na studia, na przemiot Języki i paradymaty programowania (III). Głownymi funkcjonalnościami są:
  - Scrapper, pobierający zawartość strony "https://www.finder.com/cryptocurrency-glossary", który tworzy zbiór definicji w formacie .json
  - Pobieranie aktualnych kursów kryptowalut przez API *CoinAPIv1*
  - Chatbot, prosty if-statement wykorzystujący pobrane wyżej wymienione

Pobrane dane zostają zapisane do bazy danych opartej na chmurze Azure (Azure SQL Database).

Frontend został stworzony w bibliotece Pythona, TKinter.
