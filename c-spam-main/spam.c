#include <windows.h>
#include <stdio.h>

#define ID_MESSAGE 1
#define ID_FREQUENCY 2
#define ID_DURATION 3
#define ID_START 4

char message[256];
int frequency = 1;
int duration = 1;

void typeMessage(const char *msg, int freq, int dur) {
    int iterations = freq * dur;

    for (int j = 0; j < iterations; j++) {
        for (int i = 0; msg[i] != '\0'; i++) {
            INPUT input = {0};
            input.type = INPUT_KEYBOARD;
            input.ki.wVk = 0; 
            input.ki.wScan = msg[i]; 
            input.ki.dwFlags = KEYEVENTF_UNICODE; 
            SendInput(1, &input, sizeof(INPUT));

            input.ki.dwFlags = KEYEVENTF_KEYUP; 
            SendInput(1, &input, sizeof(INPUT));
        }

        INPUT enterInput = {0};
        enterInput.type = INPUT_KEYBOARD;
        enterInput.ki.wVk = VK_RETURN; 
        SendInput(1, &enterInput, sizeof(INPUT));
        enterInput.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &enterInput, sizeof(INPUT));

        Sleep(1000); 
    }
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE:
            CreateWindow("EDIT", "", WS_CHILD | WS_VISIBLE | WS_BORDER,
                         20, 20, 200, 25, hwnd, (HMENU)ID_MESSAGE, NULL, NULL);
            CreateWindow("EDIT", "", WS_CHILD | WS_VISIBLE | WS_BORDER,
                         20, 60, 50, 25, hwnd, (HMENU)ID_FREQUENCY, NULL, NULL);
            CreateWindow("EDIT", "", WS_CHILD | WS_VISIBLE | WS_BORDER,
                         20, 100, 50, 25, hwnd, (HMENU)ID_DURATION, NULL, NULL);
            CreateWindow("BUTTON", "Başlat", WS_CHILD | WS_VISIBLE,
                         20, 140, 100, 30, hwnd, (HMENU)ID_START, NULL, NULL);
            break;
        case WM_COMMAND:
            if (LOWORD(wParam) == ID_START) {
                HWND hMessage = GetDlgItem(hwnd, ID_MESSAGE);
                HWND hFrequency = GetDlgItem(hwnd, ID_FREQUENCY);
                HWND hDuration = GetDlgItem(hwnd, ID_DURATION);

                GetWindowText(hMessage, message, sizeof(message)); // Mesajı al
                char freqStr[10], durStr[10];
                GetWindowText(hFrequency, freqStr, sizeof(freqStr)); // Frekansı al
                GetWindowText(hDuration, durStr, sizeof(durStr)); // Süreyi al
                
                frequency = atoi(freqStr); // Frekansı integer'a çevir
                duration = atoi(durStr); // Süreyi integer'a çevir

                // 5 saniye bekleyin
                Sleep(5000);
                typeMessage(message, frequency, duration);
            }
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
    const char CLASS_NAME[] = "Sample Window Class";
    WNDCLASS wc = {0};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);
    HWND hwnd = CreateWindowEx(0, CLASS_NAME, "Mesaj Yazma Aracı", WS_OVERLAPPEDWINDOW,
                               CW_USEDEFAULT, CW_USEDEFAULT, 300, 250, NULL, NULL, hInstance, NULL);

    ShowWindow(hwnd, nShowCmd);
    UpdateWindow(hwnd);

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}
