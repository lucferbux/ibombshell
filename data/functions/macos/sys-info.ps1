function sys-info {
    $infos = system_profiler SPSoftwareDataType
        
    return $infos
}