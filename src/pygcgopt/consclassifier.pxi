cdef class ConsClassifier:
    """Base class of the Constraint Classifier Plugin"""
    cdef public Model model
    cdef public str name

    def freeConsClassifier(self):
        '''calls destructor and frees memory of constraint classifier'''
        pass

    def classify(self, conss, partition):
        pass

cdef SCIP_RETCODE PyConsClassifierFree(GCG* gcg, GCG_CLSCONS* consclassifier) with gil:
    cdef GCG_CLSCONSDATA* consclassifierdata
    consclassifierdata = GCGclsconsGetData(consclassifier)
    py_consclassifier = <ConsClassifier>consclassifierdata
    py_consclassifier.freeConsClassifier()
    Py_DECREF(py_consclassifier)
    return SCIP_OKAY

cdef SCIP_RETCODE PyConsClassifierClassify(GCG* gcg, GCG_CLSCONS* consclassifier, SCIP_Bool transformed) with gil:
    cdef GCG_CLSCONSDATA* consclassifierdata
    consclassifierdata = GCGclsconsGetData(consclassifier)
    py_consclassifier = <ConsClassifier>consclassifierdata
    if transformed:
        detprobdata = py_consclassifier.model.getDetprobdataPresolved()
    else:
        detprobdata = py_consclassifier.model.getDetprobdataOrig()
    conss = detprobdata.getRelevantConss()
    partition = detprobdata.createConsPart(py_consclassifier.name, 0, len(conss))
    py_consclassifier.classify(conss, partition)
    print("Consclassifier {0} yields a classification with {1} different constraint classes".format(partition.getName(), partition.getNClasses()))
    detprobdata.addConsPartition(partition)
    return SCIP_OKAY
