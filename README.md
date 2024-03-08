# Repo YNOV B2 G1 Data

https://github.com/Gladrat/ynov_b2_g1_data

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[10];
    int age;
    bool association;
};

struct Color {
    int red;
    int green;
    int blue;
    float alpha;
}

int main() {
    struct Student student1;
    
    strcpy(student1.name, "Lisa");
    student1.age = 20;
    student1.association = true;
    
    printf("Name: %s\n", student1.name);
    printf("Age: %d\n", student1.age);
    printf("Association member: %s\n", student1.association ? "Yes" : "No");
    
    struct Color mainColor = { 39, 245, 234, 0.8 };
    
    return 0;
}
```

|   |   |    |   |
|---|---|----|---|
| 0 | 0 | 0  | 0 |
| 1 | 0 | 99 | 0 |
| 2 | 0 | 0  | 0 |
|   | 0 | 1  | 2 |