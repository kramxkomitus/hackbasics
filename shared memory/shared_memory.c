#include "stdio.h"
#include "fcntl.h"
#include "unistd.h"
#include "sys/mman.h"
#include "sys/stat.h"
#include "string.h"
void write_shared_memory();
void open_shared_memory();

const char *const shm_name = "name";

void write_shared_memory()
{
    int flag = O_RDWR | O_CREAT;
    const char *HW = "Hello World!";

    int fd = shm_open(shm_name, flag, 0666);
    ftruncate(fd, 100);

    printf("%d", fd);

    char *map_p = mmap(NULL, 100, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);   //-1 MAP_ANONYMOUS

    strcpy(map_p, HW);
    getchar();
    getchar();
    // munmap(map_p, 100);
    shm_unlink(shm_name);
    // fprintf(stderr, )
}

void open_shared_memory()
{
    char str[15];
    int flag = O_RDWR;
    int fd = shm_open(shm_name, flag, 0666);
    char *map_p = mmap(NULL, 100, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    printf("%s", map_p);
}

void main()
{
    char str[15];
    char c;
    printf("shouter: a, listener: b");
    c = getchar();
    if (c == 'a')
    {
        write_shared_memory();
    }
    else
    {
        open_shared_memory();
    }

    return 0;
}
