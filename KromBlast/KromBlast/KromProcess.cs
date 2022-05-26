using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using Microsoft.Web.WebView2;
using System.Threading;
using System.IO;

namespace KromBlast
{
    internal class KromProcess
    {
        string id;
        Process myCmd;
        List<String> myWaitedCommand;
        Microsoft.Web.WebView2.WinForms.WebView2 webView;
        StreamWriter sw;
        StreamReader sr;

        public KromProcess(String id, Microsoft.Web.WebView2.WinForms.WebView2 webView,
            List<String> myWaitedCommand
            )
        {
            this.id = id;
            this.myWaitedCommand = myWaitedCommand;
            this.webView = webView;
            myCmd = createConsole();
            sw = myCmd.StandardInput;
            sr = myCmd.StandardOutput;
            sw.AutoFlush = true;
            sw.WriteLine("@echo off");
            sw.WriteLine("cd %APPDATA%");
            sw.WriteLine("echo *end");
            string waited = "";
            do
            {
                waited = sr.ReadLine();
            } while (!waited.Equals("*end"));
            System.Windows.Forms.Timer timer1 = new System.Windows.Forms.Timer();
            timer1.Tick += new EventHandler(looper);
            timer1.Interval = 2000; // in miliseconds
            timer1.Start();
        }

        private void looper(object sender, EventArgs e)
        {
            if (myWaitedCommand.Count != 0)
            {
                myCmd.StandardInput.WriteLine(myWaitedCommand[0]);
                myCmd.StandardInput.WriteLine("echo *end");
                List<String> returned = new List<string>();
                string getting = "";
                do
                {
                    getting = sr.ReadLine();
                    returned.Add(getting);
                } while (!getting.Equals("*end"));
                foreach (string i in returned)
                {
                    webView.ExecuteScriptAsync(
                        "KromBlast.returnCmd(\"" + myWaitedCommand[0] + "\", \"" + i + "\")"
                        );
                }
                myWaitedCommand.RemoveAt(0);
            }
        }


        private Process createConsole()
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.UseShellExecute = false; //required to redirect standart input/output

            // redirects on your choice
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;
            startInfo.RedirectStandardInput = true;
            startInfo.CreateNoWindow = true;

            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "";

            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();
            return process;

            //process.StandardInput.WriteLine("");
        }
    }
}
