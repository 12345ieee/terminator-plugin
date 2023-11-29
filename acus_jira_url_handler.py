import terminatorlib.plugin as plugin

# Every plugin you want Terminator to load *must* be listed in "AVAILABLE"
AVAILABLE = ["AcusJiraURLHandler"]

class AcusJiraURLHandler(plugin.URLHandler):
    """Acus Jira URL Handler, if the token is of the form ABC-123 open it in Jira.
    We have an hardcoded project list"""
    capabilities = ["url_handler"]
    handler_name = "acus_jira"
    nameopen = "Open Jira URL"
    namecopy = "Copy Jira URL"

    # retrieved by hand on 29/11/2023
    projects = ["AA","AAA","AAC","AAI","AAM","ABDR","ABH","ABS","ACB","ACM","ACN","AD","ADK","ADR","AEC","AECC","AECS","AF","AFC","AHR","AIDK","AIDR","AM","AMK","AOT","AP","APLA","APN","AQC","ASEC","ASF","ASG","ASS","AT","ATN","ATS","AUM","BDGMAR","BDGTEC","BUGFIX","CD","CER","CL","CO","CONS","CSC","CSU","DA","DCA","DESCRG","DESCRQ","DESCS","DESDEL","DESDEV","DESMAR","DESTEST","DEVGM","DEVOP","DOC","EO","EP","EVACRG","EVACRQ","EVACSE","EVACSI","EVAG","FER","FOR","GMACE","HPD","HR","ICT","IEDEV","INFAPN","INFCA","INFCM","INFSE","JIRASUP","KT","MC","MDM","MKTG","PA","PHIACE","PHIAGS","PHIAUD","PHIAXP","PHICEI","PHIDOL","PHIDUF","PHIEGE","PHIENIEE","PHIENING","PHIENN","PHIEON","PHIEST","PHIESTR","PHIFREE","PHIHER","PHIIBE","PHIILL","PHILEV","PHIREP","PHISIN","PHIUMB","PM","PP","PROT","QAOP","QASD","REP","RFD","SCAR","SCMC","SCMG","SDAAM","SETFAS","SIACSA","SIACSU","SIAUSA","SIAXSA","SICASA","SIDUSA","SIENSA","SIEOSA","SIFESA","SIGGP","SIGNA","SIGND","SIGNG","SIGNU","SIGPA","SIHESA","SIILSA","SIIMSA","SILESA","SIMACE","SIMAIM","SIMALP","SIMANDUF","SIMANENI","SIMAUD","SIMAXP","SIMCAN","SIMDUF","SIMENE","SIMENI","SIMEON","SIMFREE","SIMIME","SIMPIU","SIMTEA","SIMUTI","SIPMACE","SIPMAXP","SIPMCAN","SIPMEON","SIPMHER","SIPMILL","SIPMLEV","SIPMREP","SIRESA","SISUP","SIUTSA","SSA","SSD","SSKO","SSR","SSS","SST","TAC","TCM","TEDEV","TM","TP","TS","TSEC"]

    match = r"\b(" + "|".join(projects) + r")-\d+\b"

    def callback(self, key):
        return "https://acus.atlassian.net/browse/" + key;
