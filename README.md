# design-explorer

<div align="center">
  <!-- Build Status -->
  <a href="https://travis-ci.org/jeremiah-c-leary/design-explorer">
    <img src="https://img.shields.io/travis/jeremiah-c-leary/design-explorer/master.svg?style=flat-square"
      alt="Build Status" />
  </a>
  <!-- Test Coverage -->
  <a href="https://codecov.io/github/jeremiah-c-leary/design-explorer">
    <img src="https://img.shields.io/codecov/c/github/jeremiah-c-leary/design-explorer/master.svg?style=flat-square"
      alt="Test Coverage" />
  </a>
  <!-- Codacy -->
  <a class="badge-align" href="https://www.codacy.com/app/jeremiah-c-leary/design-explorer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jeremiah-c-leary/design-explorer&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/42744dca97544824b93cfc99e8030063"
      alt="Codacy" />
  </a>
  <!-- Code Climate -->
  <a href="https://codeclimate.com/github/jeremiah-c-leary/design-explorer/maintainability">
    <img src="https://api.codeclimate.com/v1/badges/2815689ec945a2f70a24/maintainability"i
      alt="Code Climate" />
  </a>
</div>

Overview
--------

I believe Design-Explorer is a missing tool in the design process of hdl systems.
We have tools that can help us after the we have code, a bottom up view.
However, we do not seem to have any tools to perform a top down design.

I have used Microsoft Visio for block diagrams and Microsoft Word for documentation.
However, I believe these tools are insufficient for there given tasks.

Block diagrams are out of date the moment they are saved and commited to source control.
Word documents are difficult to manage and lock information into a hard to parse format.

Design-Explorer will attempt to provide an easy to use tool to document and explore design decisions.
It will also allow data mining to provide different visualizations of the design.

Goals
-----

I am a attempting to answer the following questions with this project:

1.  Can an hdl system be abstracted using python
2.  Can an abstracted hdl system be used to document the design
..1. Produce accurate block diagrams
..2. Provide a different vehicle to browse the documentation
3.  Can an abstracted hdl system be used to create hierarchies
4.  Can an abstracted hdl system be used to generate HDL tool inputs
5.  Can a re-usable library of components be created to aid in IP generation

Outputs
-------

1.  Graphical output of the design that can be filtered depending on what the user is looking for.
2.  HDL files that can be compiled and synthesized

