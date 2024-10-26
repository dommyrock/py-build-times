### Build times

This repo contains quick Utility scripts that visualize per project build times as well as timed .NET build pipeline steps.

<br>
Although this was used to help out with .NET based project, it can easily be tweaked for any other runtime.

### Get your 'PerformanceSummary' for .NET project

```bash
# Go to Developer console from VS --> Tools  
msbuild ./HRNet.sln /clp:PerformanceSummary
```

### MS Binary log format 
There is a great [GUI tool](https://msbuildlog.com) you can use with this format.

```bash
msbuild YourSolution.sln /bl
```
Quick way to see your top time spenders...
![Binlog top 10](/assets/Build_Top_10_MostExpensive.webp)

#### Build tasks
![Build tasks plot](/assets/build_tasks_MsBuild.webp)

#### Build projects
![Build projects plot](/assets/build_all_projects.webp)

#### Build tests
![Build tests plot](/assets/build_test_proj.webp)


#### DOCS:
- https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2022
- https://msbuildlog.com/ (Binary log GUI tool)
- https://learn.microsoft.com/en-us/shows/visual-studio-toolbox/msbuild-structured-log-viewer

