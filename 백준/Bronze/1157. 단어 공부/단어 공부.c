#include <stdio.h>

int main(){
    int alphabet_count[(int)'Z' - (int)'A' + 1] = {0};
    char words[1000000];
    scanf("%s", words);
    
    for(int i = 0; i < 1000000; i++){
        if(words[i] == '\0')
            break;
        if(words[i] >= 'a' && words[i] <= 'z')
            alphabet_count[(int)words[i] - (int)'a']++;
        else
            alphabet_count[(int)words[i] - (int)'A']++;
    }
    
    int max_count = 0, max_idx = 0;
    
    for(int i = 0; i < (int)'Z' - (int)'A' + 1; i++){
        if(max_count < alphabet_count[i]){
            max_count = alphabet_count[i];
            max_idx = i;
        }
        else if(max_count == alphabet_count[i])
            max_idx = -1;
    }
    
    if(max_idx == -1)
        printf("?");
    else
        printf("%c", (char)(max_idx +(int)'A'));
    return 0;
}
