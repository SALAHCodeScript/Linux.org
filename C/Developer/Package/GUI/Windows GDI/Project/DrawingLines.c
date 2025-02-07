#include <windows.h>

// Define a custom background brush
HBRUSH hBrush = NULL;

// Window Procedure Function
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE:
            // Create a brush with a black color (RGB(5, 5, 8))
            hBrush = CreateSolidBrush(RGB(5, 5, 8));
            break;

        case WM_ERASEBKGND: {
            // Handle background color manually
            HDC hdc = (HDC)wParam;
            RECT rect;
            GetClientRect(hwnd, &rect);
            FillRect(hdc, &rect, hBrush);
            return 1;  // Return 1 to indicate we've handled it
        }

        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // Create pens for different colors
            HPEN hGreenPen1 = CreatePen(PS_SOLID, 2, RGB(0, 150, 50));
            HPEN hGreenPen2 = CreatePen(PS_SOLID, 2, RGB(0, 150, 50));

            // Select green pen and draw the first line
            SelectObject(hdc, hGreenPen1);
            MoveToEx(hdc, 0, 0, NULL);
            LineTo(hdc, 480, 360);

            // Select green pen and draw the second line
            SelectObject(hdc, hGreenPen2);
            MoveToEx(hdc, 480, 0, NULL);
            LineTo(hdc, 0, 360);

            // Cleanup
            DeleteObject(hGreenPen1);
            DeleteObject(hGreenPen2);
            EndPaint(hwnd, &ps);
            break;
        }

        case WM_DESTROY:
            if (hBrush) DeleteObject(hBrush);  // Clean up the brush
            PostQuitMessage(0);
            return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

// WinMain: Entry Point for Windows Applications
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    const char CLASS_NAME[] = "GDIExampleWindow";

    WNDCLASS wc = {0};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);  // Default system color (won't be used due to WM_ERASEBKGND)

    RegisterClass(&wc);
    
    HWND hwnd = CreateWindowEx(0, CLASS_NAME, "GDI Background Color Example", WS_OVERLAPPEDWINDOW,
                               CW_USEDEFAULT, CW_USEDEFAULT, 500, 400,
                               NULL, NULL, hInstance, NULL);
    if (!hwnd) return 0;

    ShowWindow(hwnd, nCmdShow);

    // Message Loop
    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}
