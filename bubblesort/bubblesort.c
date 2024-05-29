void bubblesort(int* unsorted, int unsortedSize){
    int temp;
    for(int i = 0; i < unsortedSize-1; i++){ // Iterate through the array from the beginning to the second-to-last element
        for(int j = 0; j < unsortedSize-i-1; j++){ // Iterate through the unsorted part of the array
            if(unsorted[j]>unsorted[j+1]){ // If the current element is greater than the next element
                int temp = unsorted[j]; // Swap the current element with the next element
                unsorted[j]=unsorted[j+1];
                unsorted[j+1]=temp;
            }
        }
    }
}



int main(){
    int arrSize = 6;
    int arr[arrSize];
    arr[0]=6;
    arr[1]=2;
    arr[2]=4;
    arr[3]=7;
    arr[4]=1;
    arr[5]=9;
    bubblesort(arr,arrSize);
    for(int i = 0; i < arrSize; i++){
        printf("%d",arr[i]);
    }
    printf("\n");
}