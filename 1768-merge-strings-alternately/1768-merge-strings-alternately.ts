function mergeAlternately(word1: string, word2: string): string {
    const minLength: number = Math.min(word1.length, word2.length);
    
    let res: string = "";
    
    for(let i = 0; i < minLength; i++){
        res = res + word1[i] + word2[i];
    } 
    
    let additional: string = "";
    if (word1.length != word2.length){
        additional = word1.length > word2.length ? word1.slice(minLength  ) :
        word2.slice(minLength);
        
    } 
    res += additional;
    return res;
};