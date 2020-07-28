from pyspark import SparkConf, SparkContext

story = """ In the song, Maui told Moana about his amazing deeds.  Why - he pulled up the islands from the sea,
he lifted the sky, he even found fire and gave it to humans!  As a demi-god, Maui was born with
special powers. Demi-god means one parent is a god and the other is human. Maui’s father was the god
and his mother was human."""

rddStory = SparkContext.parallelize([story], c)

lengthStory = rddStory.flatMap(lambda sentence: sentence.split(" ")) \
    .filter(lambda word: word.startswith('D') or word.startswith('d')) \
    .count()
print(lengthStory)
