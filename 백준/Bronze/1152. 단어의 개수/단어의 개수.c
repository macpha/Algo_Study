#include <stdio.h>

int main(){
    int word_count = 0;
    char c = getchar(), tmp = c;
    
    while(1){
        if(tmp != ' ')
            if(c == ' ' || c == '\n')
                word_count++;
        
        if(c == '\n' || c == '\0')
            break;
        
        tmp = c;
        c = getchar();
    }

    printf("%d", word_count);
    return 0;
}
