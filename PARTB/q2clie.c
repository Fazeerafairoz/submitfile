#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080

int main() {
    int socketfd;
    struct sockaddr_in server_addr;

    // Create 
    socketfd = socket(AF_INET, SOCK_STREAM, 0);
    if (socketfd == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    // Prepare server address 
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, "127.0.0.1", &(server_addr.sin_addr)) <= 0) {
        perror("inet_pton");
        exit(EXIT_FAILURE);
    }

    // Connect 
    if (connect(socketfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("connect");
        exit(EXIT_FAILURE);
    }

    printf("Connected now to server\n");

    // Receive random number 
    int random_number;
    if (recv(socketfd, &random_number, sizeof(random_number), 0) == -1) {
        perror("recv");
        exit(EXIT_FAILURE);
    }

    printf("Has been received random number from server: %d\n", random_number);

    // Close socket
    close(socketfd);

    return 0;
}

