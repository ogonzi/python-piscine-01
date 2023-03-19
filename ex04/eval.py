class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if len(coefs) == len(words):
			return sum([len(x) * y for x, y in zip(words, coefs)])
		else:
			return -1
	
	@staticmethod
	def enumerate_value(coefs, words):
		if len(coefs) == len(words):
			return sum(len(words[i]) * coef for i, coef in enumerate((coefs)))
		else:
			return -1