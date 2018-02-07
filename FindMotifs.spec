/*
A KBase module: FindMotifs
*/

module FindMotifs {
    /*
        Insert your typespec information here.
    */
    typedef structure{

    }FindMotifsParams;

    typedef structure{

    }FindMotifsResults

    funcdef find_motifs(FindMotifsParams params)
        returns (FindMotifsResults output) authentication required;

};
