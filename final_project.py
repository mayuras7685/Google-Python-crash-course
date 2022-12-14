def calculate_frequencies(file_contents): 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~"'''
uninteresting_words = ["the", "a", "to", "if", "is", "in" "it", "of", "and", "or","on", "an", "as", "i", "me", "my", \ "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \ "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \ "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \ "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"] 
# LEARNER CODE START HERE 
frequencies = {} 
taken = [] 
for letter in punctuations: 
  file_contents = file_contents.replace(letter,'') 
for word in uninteresting_words: w = ' '+word+' ' 
  file_contents = file_contents.replace(w,' ') 
for word in file_contents.split(): 
  if word.lower() not in taken: 
    taken.append(word.lower()) 
      if word not in frequencies: 
        frequencies[word] = 1 
      else: frequencies[word] += 1 

#wordcloud 
cloud = wordcloud.WordCloud() 
cloud.generate_from_frequencies(frequencies) 
return cloud.to_array()
