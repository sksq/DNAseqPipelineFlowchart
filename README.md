# DNAseq Flowchart

> C3G GSOC'16 selection test for Flowchart creator for MUGQIC Pipelines

## Installation

1. Clone this repository using this command:

  ```
  $ git clone https://github.com/sksq/DNAseqPipelineFlowchart
  ```

2. Install `graphviz`:

  ```
  $ [sudo] apt-get install graphviz libgraphviz-dev pkg-config
  ```

3. Install python wrapper of graphviz:

  ```
  $ [sudo] pip install graphviz
  ```

4. Finally run the application:

  ```
  $ python flowchartCreator.py
  ```
The final flowchart will be stored in output directory as DNAseqPipeline.pdf.
