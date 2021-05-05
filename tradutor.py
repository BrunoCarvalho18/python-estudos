from translate import Translator

s = Translator(from_lang="english",to_lang="pt-br")

res = s.translate("Thank you for the time and effort you put into our lesson today . I applaud your enthusiasm and determination to learn and perfect your English skills. Keep practicing. I know that you will excel at English. Great work!")

print(res)