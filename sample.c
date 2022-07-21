
    res = reqArr[n+1] - reqArr[pos]; 
    printf("Access path: %d", reqArr[pos]); 
    for(i = pos+1; i <= n+1; i++){
        printf(" -> %d", reqArr[i]);
    }
    for(i = pos-1; i >= 0; i--)
        printf(" -> %d", reqArr[i]); //printing remaining nos in second line
    res += abs(dsk_sz - reqArr[pos-2]);
    printf("\nTotal Distance: %d\n", res);
    return 0;
}