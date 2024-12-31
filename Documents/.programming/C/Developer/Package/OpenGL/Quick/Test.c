#include <GL/glut.h>

// Function to draw a triangle
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_TRIANGLES);
        glColor3f(1.0, 0.0, 0.0); glVertex2f(-0.5, -0.5);
        glColor3f(0.0, 1.0, 0.0); glVertex2f(0.5, -0.5);
        glColor3f(0.0, 0.0, 1.0); glVertex2f(0.0, 0.5);
    glEnd();
    glFlush();
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutCreateWindow("Simple OpenGL Program");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
