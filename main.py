import nltk
import string
import re,os
from nltk.stem import PorterStemmer


class main:
    stop_words=[]
    ps = PorterStemmer()
    inverted_index = {}
    doc_list=[]
    docs=[]
    def __init__(self):
        pass
    
    def stemStopWords(self):
        with open('Stopword-List.txt','r') as f:
            stop_words = f.read().split()
        for i,v in enumerate(stop_words):
            stop_words[i] = self.ps.stem(v)
            
    def isConsecChar(self,val):
        count = 0
        max_count=0
        for i,v in enumerate(val):
            if i==len(val)-1 and count>0:
                count+=1
                continue
            elif i<len(val)-1:
                if v==val[i+1]:
                    count+=1
                else:
                    count=0
            if count>max_count:
                max_count = count
        return max_count+1
    
    def buildInvertedIndex(self):
        count=0
        re1=r'[a-z]+((?:-[a-z]+)*)?'
        filenames=os.listdir('ResearchPapers/')
        for i in filenames:
            doc_id=int(i.strip('.txt'))
            self.docs.append(doc_id)
            file = os.path.join('ResearchPapers',i)
            with open(file,'r',encoding='utf-8', errors='ignore') as f:
                text = f.read()
                text=text.lower().split()
                count+=len(text)
                for index, val in enumerate(text):
                    if "@" not in val and ".co" not in val and "http" not in val and self.isConsecChar(val)<3:
                        match = re.search(re1,val)
                        if match:
                            val = match.group()
                            if "-" in val and val.count('-')==1:
                                val = val.replace("-","")
                            val= self.ps.stem(val)
                            if (val not in self.stop_words) and (len(val)>1) and (len(val)<16):
                                if val in self.inverted_index:
                                    if doc_id in self.inverted_index[val]:
                                        self.inverted_index[val][doc_id].append(index)
                                    else:
                                        self.inverted_index[val][doc_id] = [index]
                                else:
                                    self.inverted_index[val] = {doc_id: [index]}
        print("Total Tokkens: ",count)
        print("Number of terms:",len(self.inverted_index))
        print("Tokkens drops: ",((count-len(self.inverted_index))/count)*100,"%")


    def intersectTerms(self,term1,term2):
        inverted_index_1 = self.inverted_index[self.ps.stem(term1)]
        inverted_index_2 = self.inverted_index[self.ps.stem(term2)]
        if len(inverted_index_1)<len(inverted_index_2):
            for i in inverted_index_1.keys():
                if i in inverted_index_2.keys():
                    self.doc_list.append(i)
        else:
            for i in inverted_index_2.keys():
                if i in inverted_index_1.keys():
                    self.doc_list.append(i)
        return self.doc_list
    
    def intersectPTerms(self,term1,term2,k):
        inverted_index_1 = self.inverted_index[self.ps.stem(term1)]
        inverted_index_2 = self.inverted_index[self.ps.stem(term2)]
        doc_list=set()
        if len(inverted_index_1)<len(inverted_index_2):
            for i in inverted_index_1.keys():
                if i in inverted_index_2.keys():
                    for x in inverted_index_1[i]:
                        for y in inverted_index_2[i]:
                            if abs(y-x)<=k:
                                doc_list.add(i)
        else:
            for i in inverted_index_2.keys():
                if i in inverted_index_1.keys():
                    for x in inverted_index_2[i]:
                        for y in inverted_index_1[i]:
                            if abs(y-x)<=k:
                                doc_list.add(i)
        return sorted(list(doc_list))
    
    def unionTerms(self,term1,term2):
        inverted_index_1 = set(self.inverted_index[self.ps.stem(term1)].keys())
        inverted_index_2 = set(self.inverted_index[self.ps.stem(term2)].keys())
        inverted_index_1.union(inverted_index_2)
        return sorted(list(inverted_index_1))
    
    def inverseTerms(self,term):
        inverted_index_set = set(self.inverted_index[self.ps.stem(term)].keys())
        return list((set(self.docs)).difference(inverted_index_set))
        
    def UserQuery(self):
        user_input = (input("Enter query: ")).lower()
        user_input_list = user_input.split()
        intersection_list=[]
        inter_lists=[]
        union_list=[]
        inverse_list=[]
        inv_list=[]
        result = set() 
        if "or" in user_input_list: 
            inter_list = user_input.split(" or ") 
            for x in inter_list: 
                if "and" in x:  # Y
                    inters = x.split(" and ") 
                    for y in inters:  
                        if "not" in y: 
                            inverse_term = y.replace("not ",'').strip() 
                            inv_list = self.inverseTerms(inverse_term) 
                        else:
                            inverse_term = y.strip() 
                            inv_list = list(self.inverted_index[self.ps.stem(inverse_term)].keys())
                        intersection_list.append(inv_list)  
                    result=set(intersection_list[0]) 
                    for x in intersection_list:
                        result = result.intersection(set(x)) 
                    intersection_list=[]
                    for i in list(result):
                        union_list.append(i)
                else: 
                    if "not" in x:  
                        inverse_term = x.replace("not ",'').strip() 
                        inv_list = self.inverseTerms(inverse_term) 
                    else: 
                        inverse_term = x.strip() 
                        inv_list = list(self.inverted_index[self.ps.stem(inverse_term)].keys()) 
                    for i in inv_list:
                        union_list.append(i) 
                
            result = set(union_list) 
            
        elif "and" in user_input_list: 
            inters = user_input.split(" and ") 
            for y in inters: 
                if "not" in y: 
                    inverse_term = y.replace("not ",'').strip()
                    inv_list = self.inverseTerms(inverse_term) 
                else:
                    inverse_term = y.strip()
                    inv_list = list(self.inverted_index[self.ps.stem(inverse_term)].keys())
                intersection_list.append(inv_list)
            result=set(intersection_list[0]) 
            for x in intersection_list:
                result = result.intersection(set(x))

        elif "not" in user_input_list:
            inverse_term = user_input.replace("not ",'').strip()
            result = self.inverseTerms(inverse_term)
            
        elif "/" in user_input:
            temp_list = user_input.split(" /")
            
            terms = temp_list[0].split()
            k = int(temp_list[1])
            result = self.intersectPTerms(terms[0],terms[1],k)
            
            
        return (sorted(list(result)))
            
                    

    
m=main()
m.stemStopWords()
m.buildInvertedIndex()
print(m.inverseTerms('transformer'))
print(m.UserQuery())



