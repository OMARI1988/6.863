
#python unigram_tagger.py ner.counts ner_dev.dat > ner_dev_unigram_tagger.dat
#python eval_ne_tagger.py ner_dev.key ner_dev_unigram_tagger.dat

#python bigram_tagger.py ner.counts ner_dev.dat > ner_dev_bigram_tagger.dat
#python eval_ne_tagger.py ner_dev.key ner_dev_bigram_tagger.dat

#python trigram_tagger.py > ner_dev_trigram_tagger.dat
#python eval_ne_tagger.py ner_dev.key ner_dev_trigram_tagger.dat

python final_tagger.py ner.counts ner_dev.dat > ner_dev_final_tagger.dat
python eval_ne_tagger.py ner_dev.key ner_dev_final_tagger.dat
