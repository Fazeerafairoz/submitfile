#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <signal.h>

#define CHILDREN 3

void handle_signal(int signum) {
    printf("Interrupt signal (%d) received by child\n", signum);
}

int main() {
    int pipefd[CHILDREN][2];
    pid_t child_pid[CHILDREN];
    int i;

    // Create pipes
    for (i = 0; i < CHILDREN; i++) {
        if (pipe(pipefd[i]) == -1) {
            perror("pipe");
            exit(EXIT_FAILURE);
        }
    }

    // Create child processes
    for (i = 0; i < CHILDREN; i++) {
        child_pid[i] = fork();

        if (child_pid[i] == -1) {
            perror("fork");
            exit(EXIT_FAILURE);
        } else if (child_pid[i] == 0) {
            // Child process
            close(pipefd[i][1]); // Close write end of the pipe

            struct sigaction sa;
            sa.sa_handler = handle_signal;
            sigemptyset(&sa.sa_mask);
            sa.sa_flags = 0;
            sigaction(SIGINT, &sa, NULL); // Register signal handler

            char message[100];
            ssize_t nbytes = read(pipefd[i][0], message, sizeof(message));
            if (nbytes > 0) {
                printf("Child %d received message: %s\n", i+1, message);
            }

            close(pipefd[i][0]); // Close read end of the pipe
            exit(EXIT_SUCCESS);
        }
    }

    // Parent process
    for (i = 0; i < CHILDREN; i++) {
        close(pipefd[i][0]); // Close read end of the pipe

        char message[100];
        sprintf(message, "This is a message from parent to child %d", i+1);
        ssize_t nbytes = write(pipefd[i][1], message, strlen(message) + 1);
        if (nbytes == -1) {
            perror("write");
            exit(EXIT_FAILURE);
        }

        close(pipefd[i][1]); // Close write end of the pipe
    }

    // Wait for child processes to finish
    for (i = 0; i < CHILDREN; i++) {
        waitpid(child_pid[i], NULL, 0);
    }

    return 0;
}

