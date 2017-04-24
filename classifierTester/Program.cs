using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Scripting.Hosting;
using IronPython.Hosting;

namespace classifierTester
{
    class Program
    {
        static void Main(string[] args)
        {
            var engine = Python.CreateEngine();
            var source=engine.CreateScriptSourceFromFile(@"classifier.py");
            var scope=engine.CreateScope();
            source.Execute(scope);
            var Classifier = scope.GetVariable("Classifier");
            var classifier = Classifier();
            classifier.addName("Libai");
            classifier.addName("wangliang");
            var items=classifier.classify();
            Console.WriteLine(items[0][0]);
            Console.ReadKey();
        }
    }
}
