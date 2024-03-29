#!/usr/bin/env python
#
# "SMT Demo"
# -----------------------------------------------------------------------------

from align import IBM1, LanguageModel

if __name__ == '__main__':

################## TRAIN TRANSLATION MODEL ##################
	my_model = IBM1('data/hansardstoy.f', \
					'data/hansardstoy.e')
	my_model.em_train(10)

	# TEST OUTPUT #
	my_model.show_alignment(my_model.align_training_data())
	print
	print "SOME TRANSLATION MODEL PROBABILITIES..."
	print my_model['OUI']['YES']
	print my_model['IL']['HE']
	print my_model['IL']['IT']
	print my_model['NATIONALE']['NATIONAL']
	print my_model['BILINGUISME']['BILINGUALISM']
	print

################## TRAIN LANGUAGE MODEL ##################
	my_lm = LanguageModel('data/hansards.e')
	my_lm.estimate_probs()

	# TEST OUTPUT #
	print
	print "Printing some trigram probabilities..."
	print my_lm['<START>']
	print
	print my_lm['he']
	print
	print my_lm['radio']

