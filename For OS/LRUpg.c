#include<stdio.h>
int main(){
int i, m, n, position, k, l, frames[10], total_frames, pages[50], total_pages, a = 0, b = 0, page_fault = 0;
printf("\nEnter number of Pages: ");
scanf("%d", &total_pages);
printf("\nEnter number of Frames: ");
scanf("%d", &total_frames);
int temp[total_frames];
for(i = 0; i < total_frames; i++)
    frames[i] = -1;
printf("\nEnter Ref String: ");
for(n = 1; n <= total_pages; n++){
    scanf("%d", &pages[n]);
            a = 0, b = 0;
            for(m = 0; m < total_frames; m++)
            {
                if(frames[m] == pages[n])
                {
                        a = 1;
                        b = 1;
                        break;
                }
            }
            if(a == 0)
            {
                for(m = 0; m < total_frames; m++)
                {
                    if(frames[m] == -1)
                    {
                        frames[m] = pages[n];
                        b = 1;
                        page_fault++;
                        break;
                    }
                }
            }
            if(b == 0)
            {
                for(m = 0; m < total_frames; m++)
                {
                    temp[m] = 0;
                }
                for(k = n - 1, l = 1; l <= total_frames - 1; l++, k--)
                {
                    for(m = 0; m < total_frames; m++)
                    {
                        if(frames[m] == pages[k])
                        {
                            temp[m] = 1;
                        }
                    }
                }
                for(m = 0; m < total_frames; m++)
                {
                    if(temp[m] == 0)
                        position = m;
                }
                frames[position] = pages[n];
                page_fault++;
            }
            
            for(m = 0; m < total_frames; m++)
            {
                printf("%d\t", frames[m]);
            }
            printf("\n");
    }
    printf("\nTotal Page Faults: %d", page_fault);
    return 0;
}