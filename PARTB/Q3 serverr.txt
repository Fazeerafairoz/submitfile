#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
#define MIN_RANGE 50000
#define MAX_RANGE 80000

int main() {
    int socketfd, new_socketfd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);

    // Create socket
    socketfd = socket(AF_INET, SOCK_STREAM, 0);
    if (socketfd == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    // Prepare server address 
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Bind 
    if (bind(socketfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("bind");
        exit(EXIT_FAILURE);
    }

    // Listen 
    if (listen(socketfd, 1) == -1) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Server is listening on port %d\n", PORT);

    // Accept
    new_socketfd = accept(socketfd, (struct sockaddr*)&client_addr, &addr_len);
    if (new_socketfd == -1) {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    printf("Client connected\n");

    // Generate random number
    int random_number = (rand() % (MAX_RANGE - MIN_RANGE + 1)) + MIN_RANGE;

    // Send random number 
    if (send(new_socketfd, &random_number, sizeof(random_number), 0) == -1) {
        perror("send");
        exit(EXIT_FAILURE);
    }

    printf("Random number has been sent to client: %d\n", random_number);

    // Close 
    close(new_socketfd);
    close(socketfd);

    return 0;
}

