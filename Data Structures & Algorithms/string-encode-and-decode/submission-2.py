class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded +str(len(s))+','

        encoded = encoded[:-1]+ '#'
        for s in strs:
            encoded = encoded+s
        print(encoded)    
        return encoded        


    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        metadata=""
        while s[i] !='#': 
            metadata+=s[i]
            i+=1
               
        i+=1
        section_len = metadata.split(',')
        print(f"section_len {section_len} : {len(section_len)}")
        if section_len[0]=='':
            return res
        j=0
        while j<len(section_len)  and i<len(s)+1:
            if int(section_len[j])==0:
                res.append("")
            else:    
                res.append(s[i:i+int(section_len[j])])
            i+=int(section_len[j])
            j+=1
        return res    




