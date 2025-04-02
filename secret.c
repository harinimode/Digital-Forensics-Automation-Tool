#include <stdio.h>
#include <string.h>

// Hidden function that is not referenced in main()
void hidden_admin_access() {
    printf("Administrator access granted!\n");
}

int main() {
    char password[20];

    printf("Enter password: ");
    scanf("%s", password);

    if (strcmp(password, "guest") == 0) {
        printf("Access Denied!\n");
    } else {
        printf("Invalid Password!\n");
    }

    return 0;
}
