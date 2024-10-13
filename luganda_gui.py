#ifndef LUGANDAIFVYPF_H
#define LUGANDAIFVYPF_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *Title;
    QToolButton *toolButton;
    QLabel *Resources;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(800, 634);
        MainWindow->setAutoFillBackground(false);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        Title = new QLabel(centralwidget);
        Title->setObjectName(QStringLiteral("Title"));
        Title->setGeometry(QRect(190, 10, 341, 91));
        QFont font;
        font.setPointSize(18);
        font.setBold(true);
        font.setWeight(75);
        Title->setFont(font);
        Title->setFrameShape(QFrame::Box);
        Title->setFrameShadow(QFrame::Raised);
        Title->setLineWidth(2);
        Title->setAlignment(Qt::AlignCenter);
        Title->setMargin(10);
        toolButton = new QToolButton(centralwidget);
        toolButton->setObjectName(QStringLiteral("toolButton"));
        toolButton->setGeometry(QRect(30, 40, 61, 51));
        toolButton->setStyleSheet(QLatin1String("*{\n"
"  font-family:century gothic;\n"
"  font-size:24px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
" background\n"
"}"));
        Resources = new QLabel(centralwidget);
        Resources->setObjectName(QStringLiteral("Resources"));
        Resources->setGeometry(QRect(80, 120, 91, 81));
        Resources->setPixmap(QPixmap(QString::fromUtf8("kissclipart-writing-resources-clipart-writing-citation-clip-ar-30f70e680b2bfd44.png")));
        Resources->setScaledContents(true);
        label = new QLabel(centralwidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(220, 120, 91, 81));
        label->setPixmap(QPixmap(QString::fromUtf8("lessons-balloons-indicates-educating-learned-childhood-representing-bunch-university-college-46492877.jpg")));
        label->setScaledContents(true);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(380, 120, 91, 81));
        label_2->setPixmap(QPixmap(QString::fromUtf8("maxresdefault.jpg")));
        label_2->setScaledContents(true);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(540, 120, 91, 81));
        label_3->setPixmap(QPixmap(QString::fromUtf8("Verb.png")));
        label_3->setScaledContents(true);
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(80, 230, 91, 81));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        label_4->setFont(font1);
        label_4->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_4->setTextFormat(Qt::PlainText);
        label_4->setAlignment(Qt::AlignCenter);
        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(230, 230, 91, 81));
        label_5->setFont(font1);
        label_5->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_5->setTextFormat(Qt::PlainText);
        label_5->setAlignment(Qt::AlignCenter);
        label_6 = new QLabel(centralwidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(380, 230, 91, 81));
        label_6->setFont(font1);
        label_6->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_6->setTextFormat(Qt::PlainText);
        label_6->setAlignment(Qt::AlignCenter);
        label_7 = new QLabel(centralwidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(540, 230, 91, 81));
        label_7->setFont(font1);
        label_7->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_7->setTextFormat(Qt::PlainText);
        label_7->setAlignment(Qt::AlignCenter);
        label_8 = new QLabel(centralwidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(80, 360, 91, 81));
        label_8->setFont(font1);
        label_8->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_8->setTextFormat(Qt::PlainText);
        label_8->setAlignment(Qt::AlignCenter);
        label_9 = new QLabel(centralwidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(230, 360, 91, 81));
        label_9->setFont(font1);
        label_9->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_9->setTextFormat(Qt::PlainText);
        label_9->setAlignment(Qt::AlignCenter);
        label_10 = new QLabel(centralwidget);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(380, 360, 91, 81));
        label_10->setFont(font1);
        label_10->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_10->setTextFormat(Qt::PlainText);
        label_10->setAlignment(Qt::AlignCenter);
        label_11 = new QLabel(centralwidget);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(540, 360, 91, 81));
        label_11->setFont(font1);
        label_11->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_11->setTextFormat(Qt::PlainText);
        label_11->setAlignment(Qt::AlignCenter);
        label_12 = new QLabel(centralwidget);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(310, 480, 101, 81));
        label_12->setFont(font1);
        label_12->setStyleSheet(QLatin1String(";\n"
"background-color: rgb(85, 85, 255);\n"
"border-color: rgb(0, 0, 0);"));
        label_12->setTextFormat(Qt::PlainText);
        label_12->setAlignment(Qt::AlignCenter);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 26));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        Title->setText(QApplication::translate("MainWindow", "Learn Luganda", nullptr));
        toolButton->setText(QApplication::translate("MainWindow", "...", nullptr));
        Resources->setText(QString());
        label->setText(QString());
        label_2->setText(QString());
        label_3->setText(QString());
        label_4->setText(QApplication::translate("MainWindow", "Class 1", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "Class 2", nullptr));
        label_6->setText(QApplication::translate("MainWindow", "Class 3", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "Class 4", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "Class 5", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "Class 6", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "Class 7", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "Class 9", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "Class 10", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // LUGANDAIFVYPF_H
