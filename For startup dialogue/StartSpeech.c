#include <stdafx.h>
#include <strsafe.h>
#include <MMSystem.h>
#pragma comment(lib, "winmm.lib")

void main() {
     PlaySound(TEXT("File path.wav"), NULL, SND_FILENAME | SND_LOOP);
}