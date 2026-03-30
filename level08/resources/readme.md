en décompilant avec ghidra:

int main(int argc,char **argv,char **envp)

{
  char *pcVar1;
  int __fd;
  size_t __n;
  ssize_t sVar2;
  int in_GS_OFFSET;
  undefined1 local_414 [1024];
  int local_14;
  
                    /* Unresolved local var: char[1024] buf@[DW_OP_breg4(ESP): +44]
                       Unresolved local var: int fd@[DW_OP_breg4(ESP): +36]
                       Unresolved local var: int rc@[DW_OP_breg4(ESP): +40] */
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (argc == 1) {
    printf("%s [file to read]\n",*argv);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  pcVar1 = strstr(argv[1],"token");
  if (pcVar1 != (char *)0x0) {
    printf("You may not access \'%s\'\n",argv[1]);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  __fd = open(argv[1],0);
  if (__fd == -1) {
    err(1,"Unable to open %s",argv[1]);
  }
  __n = read(__fd,local_414,0x400);
  if (__n == 0xffffffff) {
    err(1,"Unable to read fd %d",__fd);
  }
  sVar2 = write(1,local_414,__n);
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return sVar2;
}

 on se rend compte
que le programme permet de lire un fichier avec l'utilisateur flag08.
cependant il regarde seulement le nom du fichier sans se soucier des symlink.

Il suffit donc de créer un symlink pour bypass la verification de nom et ainsi pouvoir lire le contenu du fichier token

ln -s token coucou
level08@SnowCrash:~$ ls
coucou  level08  token
level08@SnowCrash:~$ ./level08 coucou
quif5eloekouj29ke0vouxean

mdp pour flag08