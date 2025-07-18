def count_words(text):
   num_of_world = text.split( )  
   return len(num_of_world)    

def char_counter(text):
    txt = text.lower()
    char_count = {}
    for char in txt:
        if char in char_count:
           char_count[char]+=1
        else: 
            char_count[char] =1
    return char_count    


        

def sort_char(value):
    char_list = [{"char": char, "num": count} for char, count in value.items() if char.isalpha()]
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list


            
